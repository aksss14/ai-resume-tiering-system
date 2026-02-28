def generate_questions(profile_summary: str, tier: str):

    if tier == "A":
        return [
            "Design a scalable distributed system for real-time processing.",
            "What trade-offs exist between consistency and availability?",
            "How would you optimize a high-throughput pipeline?",
            "Explain system bottleneck detection strategies.",
            "How would you design for failure recovery?"
        ]

    elif tier == "B":
        return [
            "Explain how REST APIs work.",
            "How do you structure a backend service?",
            "What is dependency injection?",
            "How do you handle errors in APIs?",
            "Explain database indexing."
        ]

    else:
        return [
            "What is an API?",
            "Explain basic HTTP methods.",
            "What is a database?",
            "What is object-oriented programming?",
            "Explain JSON."
        ]