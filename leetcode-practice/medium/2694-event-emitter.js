// 2694. Event Emitter (Medium)
// https://leetcode.com/problems/event-emitter/
// Submission 2201042054 -- Accepted, JavaScript
// My thinking: I keep a list of listeners per event —
// subscribing adds one and hands back an unsubscribe
// that removes it, and emitting calls each listener in
// the order they subscribed.
class EventEmitter {
    constructor() {
        this.events = {};
    }

    subscribe(eventName, callback) {
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }
        this.events[eventName].push(callback);
        return {
            unsubscribe: () => {
                this.events[eventName] = this.events[eventName].filter(
                    (cb) => cb !== callback
                );
            },
        };
    }

    emit(eventName, args = []) {
        const listeners = this.events[eventName] || [];
        return listeners.map((callback) => callback(...args));
    }
}
