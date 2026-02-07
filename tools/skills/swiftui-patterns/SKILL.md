---
name: ios-swiftui-patterns
description: Advanced SwiftUI optimization techniques for smooth, responsive interfaces. Use when SwiftUI views render slowly, animations drop frames, or memory usage is higher than expected.
---

# SwiftUI Performance Patterns

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

## Best Practices

- **Measurement First**: Profile with Instruments before optimizing
- **Structural Identity**: Maintain stable view hierarchies for diffing efficiency
- **Minimize Recomputation**: Cache expensive calculations outside of view body
- **Memory Management**: Properly manage @StateObject and @ObservedObject lifecycles

## Common Pitfalls

- **View Body Complexity**: Expensive operations cause frequent re-computation
- **State Over-Invalidation**: Too broad @Published properties triggering unnecessary updates
- **Image Memory Leaks**: Not properly managing large image assets in lists
- **Animation Layering**: Multiple simultaneous animations causing frame drops

## Implementation Examples

**Optimized List with Lazy Loading:**
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
```

**Efficient State Management:**
```swift
class AlertViewModel: ObservableObject {
    @Published private(set) var alerts: [Alert] = []
    @Published private(set) var isLoading: Bool = false
    @Published private(set) var unreadCount: Int = 0
    
    private var allAlerts: [Alert] = [] {
        didSet {
            let newAlerts = allAlerts.filter(\.isVisible)
            if newAlerts != alerts { alerts = newAlerts }
            let newCount = allAlerts.filter(\.isUnread).count
            if newCount != unreadCount { unreadCount = newCount }
        }
    }
}
```

## Resources

- Apple's SwiftUI performance documentation
- Xcode Instruments for profiling
- Swift forums performance discussions
