# SwiftUI Performance Patterns

| name | description | domain | complexity |
|------|-------------|--------|------------|
| swiftui-performance-patterns | Advanced SwiftUI optimization techniques for smooth, responsive user interfaces | frontend | intermediate |

## When to Use This Skill
When SwiftUI views are rendering slowly, animations are dropping frames, or memory usage is higher than expected in iOS applications.

## Core Concepts

**View Body Optimization:**
- Minimize expensive computations in view body
- Use computed properties and lazy evaluation
- Avoid complex state transformations during rendering
- Leverage SwiftUI's structural identity system

**State Management Efficiency:**
- Choose appropriate property wrappers (@State, @StateObject, @ObservedObject)
- Minimize unnecessary view updates through precise state modeling
- Use @Published selectively to avoid over-invalidation
- Implement custom Equatable for complex state objects

**List and Grid Performance:**
- LazyVStack/LazyHStack for large datasets
- Proper cell reuse patterns
- Image loading and caching strategies
- Pagination and data virtualization

**Animation Optimization:**
- GPU vs CPU animation decisions
- Implicit vs explicit animation performance
- View modifier order for animation efficiency
- Custom animation timing and easing

## Best Practices
- **Measurement First**: Profile with Instruments before optimizing
- **Structural Identity**: Maintain stable view hierarchies for diffing efficiency
- **Minimize Recomputation**: Cache expensive calculations outside of view body
- **Memory Management**: Properly manage @StateObject and @ObservedObject lifecycles

## Common Pitfalls
- **View Body Complexity**: Expensive operations in view body cause frequent re-computation
- **State Over-Invalidation**: Too broad @Published properties triggering unnecessary updates
- **Image Memory Leaks**: Not properly managing large image assets in lists
- **Animation Layering**: Multiple simultaneous animations causing frame drops

## Implementation Examples

**Example 1**: Optimized List with Lazy Loading
```swift
struct OptimizedEventList: View {
    @StateObject private var viewModel = EventListViewModel()
    
    var body: some View {
        LazyVStack(spacing: 0) {
            ForEach(viewModel.visibleEvents) { event in
                EventRowView(event: event)
                    .onAppear {
                        viewModel.loadMoreIfNeeded(event: event)
                    }
            }
        }
    }
}

struct EventRowView: View {
    let event: Event
    @State private var image: UIImage?
    
    var body: some View {
        HStack {
            AsyncImage(url: event.imageURL) { image in
                image
                    .resizable()
                    .aspectRatio(contentMode: .fill)
            } placeholder: {
                Rectangle()
                    .fill(Color.gray.opacity(0.3))
            }
            .frame(width: 60, height: 60)
            .clipped()
            
            VStack(alignment: .leading) {
                Text(event.title)
                    .font(.headline)
                Text(event.subtitle)
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            Spacer()
        }
        .padding(.horizontal)
    }
}
```

**Example 2**: Efficient State Management
```swift
class AlertViewModel: ObservableObject {
    @Published private(set) var alerts: [Alert] = []
    @Published private(set) var isLoading: Bool = false
    
    // Separate published properties to minimize updates
    @Published private(set) var unreadCount: Int = 0
    
    private var allAlerts: [Alert] = [] {
        didSet {
            // Only update published properties when necessary
            let newAlerts = allAlerts.filter(\.isVisible)
            if newAlerts != alerts {
                alerts = newAlerts
            }
            
            let newUnreadCount = allAlerts.filter(\.isUnread).count
            if newUnreadCount != unreadCount {
                unreadCount = newUnreadCount
            }
        }
    }
    
    func loadAlerts() {
        guard !isLoading else { return }
        isLoading = true
        
        AlertService.fetchAlerts { [weak self] result in
            DispatchQueue.main.async {
                self?.isLoading = false
                switch result {
                case .success(let alerts):
                    self?.allAlerts = alerts
                case .failure(let error):
                    // Handle error
                    break
                }
            }
        }
    }
}
```

**Example 3**: Performance-Optimized Animation
```swift
struct AnimatedAlertCard: View {
    let alert: Alert
    @State private var isExpanded: Bool = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text(alert.title)
                    .font(.headline)
                Spacer()
                Button(action: { isExpanded.toggle() }) {
                    Image(systemName: "chevron.down")
                        .rotationEffect(.degrees(isExpanded ? 180 : 0))
                        .animation(.spring(response: 0.3), value: isExpanded)
                }
            }
            
            if isExpanded {
                Text(alert.description)
                    .font(.body)
                    .transition(.opacity.combined(with: .move(edge: .top)))
            }
        }
        .padding()
        .background(Color.secondary.opacity(0.1))
        .cornerRadius(12)
        .animation(.spring(response: 0.4, dampingFraction: 0.8), value: isExpanded)
    }
}
```

**Example 4**: Memory-Efficient Image Handling
```swift
struct CachedAsyncImage: View {
    let url: URL?
    let placeholder: Image
    
    @StateObject private var imageLoader = ImageLoader()
    
    var body: some View {
        Group {
            if let image = imageLoader.image {
                Image(uiImage: image)
                    .resizable()
            } else {
                placeholder
                    .foregroundColor(.gray)
            }
        }
        .onAppear {
            imageLoader.load(from: url)
        }
        .onDisappear {
            imageLoader.cancel()
        }
    }
}

class ImageLoader: ObservableObject {
    @Published var image: UIImage?
    private var cancellable: URLSessionDataTask?
    
    func load(from url: URL?) {
        guard let url = url else { return }
        
        // Check cache first
        if let cachedImage = ImageCache.shared.image(for: url) {
            self.image = cachedImage
            return
        }
        
        cancellable = URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let image = UIImage(data: data) else { return }
            
            DispatchQueue.main.async {
                ImageCache.shared.store(image, for: url)
                self.image = image
            }
        }
        cancellable?.resume()
    }
    
    func cancel() {
        cancellable?.cancel()
        cancellable = nil
    }
}
```

## Resources
- **Books**: "SwiftUI by Example" performance chapters
- **Documentation**: Apple's SwiftUI performance documentation
- **Tools**: Xcode Instruments, SwiftUI debugging tools
- **Communities**: r/SwiftUI, Swift forums performance discussions