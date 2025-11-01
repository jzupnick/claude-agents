# Emergency Alert Protocols

| name | description | domain | complexity |
|------|-------------|--------|------------|
| emergency-alert-protocols | Knowledge of government emergency alert systems, protocols, and compliance requirements | backend | advanced |

## When to Use This Skill
When implementing government emergency alert integrations, ensuring compliance with federal standards, or building life-safety critical notification systems.

## Core Concepts

**Common Alerting Protocol (CAP):**
- XML-based data format for emergency information exchange
- Standardized message structure for interoperability
- Event classification and severity levels
- Geographic targeting and distribution methods

**Emergency Alert System (EAS):**
- Federal emergency broadcasting infrastructure
- Integration points for digital platforms
- Message prioritization and override mechanisms
- Compliance requirements for participating systems

**Wireless Emergency Alerts (WEA):**
- Cell broadcast technology for mobile devices
- Message length and formatting constraints
- Geographic targeting capabilities
- Opt-out restrictions for Presidential alerts

**Alert Distribution Architecture:**
- Multi-channel delivery mechanisms
- Redundancy and failover strategies
- Real-time message routing and filtering
- Audit trail and logging requirements

## Best Practices
- **Message Clarity**: Use clear, actionable language that works across all demographics
- **Geographic Precision**: Target alerts to specific areas to avoid alert fatigue
- **Redundant Delivery**: Implement multiple delivery channels for critical alerts
- **Compliance Testing**: Regular testing of alert delivery mechanisms and timing

## Common Pitfalls
- **Over-alerting**: Sending too many non-critical alerts reduces user attention to real emergencies
- **Geographic Overshoot**: Alerts reaching areas outside the danger zone causing unnecessary panic
- **Technical Dependencies**: Single points of failure in alert delivery infrastructure
- **Accessibility Gaps**: Missing support for users with disabilities in alert presentation

## Implementation Examples

**Example 1**: CAP Message Processing
```xml
<?xml version="1.0" encoding="UTF-8"?>
<alert xmlns="urn:oasis:names:tc:emergency:cap:1.2">
    <identifier>43b080713727</identifier>
    <sender>hsas@dhs.gov</sender>
    <sent>2025-11-01T14:39:01-05:00</sent>
    <status>Actual</status>
    <msgType>Alert</msgType>
    <scope>Public</scope>
    <info>
        <category>Security</category>
        <event>Homeland Security Advisory System Update</event>
        <urgency>Expected</urgency>
        <severity>Moderate</severity>
        <certainty>Likely</certainty>
        <area>
            <areaDesc>U.S. nationwide</areaDesc>
            <geocode>
                <valueName>FIPS6</valueName>
                <value>001001</value>
            </geocode>
        </area>
    </info>
</alert>
```

**Example 2**: iOS WEA Integration
```swift
import UserNotifications
import EmergencyAlerts

class EmergencyAlertManager {
    func processWEAMessage(_ capMessage: CAPMessage) {
        let content = UNMutableNotificationContent()
        content.title = capMessage.event
        content.body = capMessage.description
        content.sound = .defaultCritical
        content.interruptionLevel = .critical
        
        // Override Do Not Disturb for emergency alerts
        content.categoryIdentifier = "EMERGENCY_ALERT"
        
        let request = UNNotificationRequest(
            identifier: capMessage.identifier,
            content: content,
            trigger: nil // Immediate delivery
        )
        
        UNUserNotificationCenter.current().add(request)
    }
}
```

**Example 3**: Geographic Targeting Logic
```swift
func shouldDeliverAlert(_ alert: EmergencyAlert, to location: CLLocation) -> Bool {
    // Check if user location intersects with alert area
    for area in alert.targetAreas {
        if area.polygon.contains(location.coordinate) {
            return true
        }
        
        // Check proximity for border cases
        let distance = location.distance(from: area.center)
        if distance <= area.radiusMeters + alertBuffer {
            return true
        }
    }
    return false
}
```

## Resources
- **Standards**: OASIS Common Alerting Protocol (CAP) v1.2 specification
- **Documentation**: FEMA Integrated Public Alert & Warning System (IPAWS) guidelines
- **Tools**: CAP message validators, alert testing frameworks
- **Communities**: Emergency Management forums, FEMA developer resources