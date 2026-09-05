"""
SignalNoise
===========

A small Python OOP system for separating useful information from
irrelevant information.

Real-life problem:
When people receive many messages, observations, alerts, feedback items,
or pieces of information, everything can look equally important.

SignalNoise helps classify information based on relevance, urgency,
reliability, and impact so that useful signals can be prioritized.
"""


class SignalNoise:
    """Stores and analyzes information items."""

    def __init__(self):
        self.sources = {}

    def create_source(self, source_id, name, description):
        """Create a source of information."""
        if source_id in self.sources:
            return False, "Source ID already exists."

        self.sources[source_id] = {
            "name": name,
            "description": description,
            "items": []
        }

        return True, "Source created successfully."

    def add_item(
        self,
        source_id,
        content,
        relevance,
        urgency,
        reliability,
        impact,
        category
    ):
        """Add an information item to a source."""
        if source_id not in self.sources:
            return False, "Source not found."

        values = {
            "relevance": relevance,
            "urgency": urgency,
            "reliability": reliability,
            "impact": impact
        }

        for field, value in values.items():
            try:
                value = int(value)
            except (ValueError, TypeError):
                return False, f"{field.title()} must be a number."

            if value < 1 or value > 5:
                return False, f"{field.title()} must be between 1 and 5."

            values[field] = value

        item = {
            "content": content,
            "relevance": values["relevance"],
            "urgency": values["urgency"],
            "reliability": values["reliability"],
            "impact": values["impact"],
            "category": category
        }

        item["signal_score"] = self.calculate_item_score(item)

        self.sources[source_id]["items"].append(item)

        return True, "Information item added successfully."

    def calculate_item_score(self, item):
        """
        Calculate the usefulness score of an information item.

        Higher relevance, urgency, reliability, and impact increase
        the signal score.

        Maximum score = 100.
        """
        relevance = item["relevance"]
        urgency = item["urgency"]
        reliability = item["reliability"]
        impact = item["impact"]

        score = (
            relevance * 0.30
            + urgency * 0.20
            + reliability * 0.25
            + impact * 0.25
        )

        return round((score / 5) * 100, 2)

    def get_source(self, source_id):
        """Return a source."""
        return self.sources.get(source_id)

    def get_signal_items(self, source_id):
        """Return items classified as useful signals."""
        source = self.get_source(source_id)

        if not source:
            return []

        return [
            item
            for item in source["items"]
            if item["signal_score"] >= 60
        ]

    def get_noise_items(self, source_id):
        """Return items classified as low-value noise."""
        source = self.get_source(source_id)

        if not source:
            return []

        return [
            item
            for item in source["items"]
            if item["signal_score"] < 40
        ]

    def get_review_items(self, source_id):
        """Return items that need human review."""
        source = self.get_source(source_id)

        if not source:
            return []

        return [
            item
            for item in source["items"]
            if 40 <= item["signal_score"] < 60
        ]

    def classify_item(self, item):
        """Classify one item."""
        score = item["signal_score"]

        if score >= 60:
            return "Signal"

        if score < 40:
            return "Noise"

        return "Needs Review"

    def get_high_priority_items(self, source_id):
        """Return highly relevant and urgent information."""
        source = self.get_source(source_id)

        if not source:
            return []

        return [
            item
            for item in source["items"]
            if (
                item["relevance"] >= 4
                and item["urgency"] >= 4
                and item["signal_score"] >= 60
            )
        ]

    def get_average_signal_score(self, source_id):
        """Calculate the average score of all information."""
        source = self.get_source(source_id)

        if not source or not source["items"]:
            return 0

        total = sum(
            item["signal_score"]
            for item in source["items"]
        )

        return round(total / len(source["items"]), 2)

    def get_category_summary(self, source_id):
        """Summarize signal scores by category."""
        source = self.get_source(source_id)

        if not source:
            return {}

        summary = {}

        for item in source["items"]:
            category = item["category"]

            if category not in summary:
                summary[category] = {
                    "count": 0,
                    "total_score": 0
                }

            summary[category]["count"] += 1
            summary[category]["total_score"] += item["signal_score"]

        for category in summary:
            count = summary[category]["count"]

            summary[category]["average_score"] = round(
                summary[category]["total_score"] / count,
                2
            )

        return summary

    def get_signal_ratio(self, source_id):
        """Calculate the percentage of information classified as signal."""
        source = self.get_source(source_id)

        if not source or not source["items"]:
            return 0

        signal_count = len(self.get_signal_items(source_id))
        total_count = len(source["items"])

        return round(
            (signal_count / total_count) * 100,
            2
        )

    def generate_recommendation(self, source_id):
        """Generate a recommendation based on the information mix."""
        source = self.get_source(source_id)

        if not source:
            return "Source not found."

        if not source["items"]:
            return (
                "No information has been recorded. "
                "Add information before analyzing the source."
            )

        signal_count = len(self.get_signal_items(source_id))
        noise_count = len(self.get_noise_items(source_id))
        review_count = len(self.get_review_items(source_id))

        total = len(source["items"])

        signal_ratio = (signal_count / total) * 100

        if signal_ratio >= 70:
            return (
                "The source contains mostly useful information. "
                "Prioritize the strongest signals."
            )

        if noise_count > signal_count:
            return (
                "A large amount of low-value information is present. "
                "Filter the noise before making decisions."
            )

        if review_count > signal_count:
            return (
                "Many items are borderline. Review their relevance "
                "and reliability before ignoring or prioritizing them."
            )

        return (
            "The information contains a mixture of signal and noise. "
            "Prioritize high-scoring items and review uncertain items."
        )

    def analyze_source(self, source_id):
        """Return a complete analysis of a source."""
        source = self.get_source(source_id)

        if not source:
            return None

        return {
            "id": source_id,
            "name": source["name"],
            "description": source["description"],
            "total_items": len(source["items"]),
            "signal_count": len(self.get_signal_items(source_id)),
            "noise_count": len(self.get_noise_items(source_id)),
            "review_count": len(self.get_review_items(source_id)),
            "high_priority_count": len(
                self.get_high_priority_items(source_id)
            ),
            "average_score": self.get_average_signal_score(source_id),
            "signal_ratio": self.get_signal_ratio(source_id),
            "category_summary": self.get_category_summary(source_id),
            "recommendation": self.generate_recommendation(source_id)
        }

    def display_source(self, source_id):
        """Display complete source analysis."""
        analysis = self.analyze_source(source_id)

        if not analysis:
            print("\nSource not found.")
            return

        print("\n" + "=" * 60)
        print("SIGNALNOISE ANALYSIS")
        print("=" * 60)

        print(f"ID: {analysis['id']}")
        print(f"Name: {analysis['name']}")
        print(f"Description: {analysis['description']}")

        print(f"\nTotal Information: {analysis['total_items']}")
        print(f"Signal: {analysis['signal_count']}")
        print(f"Noise: {analysis['noise_count']}")
        print(f"Needs Review: {analysis['review_count']}")
        print(
            f"High Priority: {analysis['high_priority_count']}"
        )
        print(f"Average Score: {analysis['average_score']}")
        print(f"Signal Ratio: {analysis['signal_ratio']}%")

        print("\nInformation:")

        if not self.sources[source_id]["items"]:
            print("  No information recorded.")
        else:
            for number, item in enumerate(
                self.sources[source_id]["items"],
                start=1
            ):
                classification = self.classify_item(item)

                print(f"\n  {number}. {item['content']}")
                print(f"     Category: {item['category']}")
                print(f"     Relevance: {item['relevance']}/5")
                print(f"     Urgency: {item['urgency']}/5")
                print(f"     Reliability: {item['reliability']}/5")
                print(f"     Impact: {item['impact']}/5")
                print(f"     Score: {item['signal_score']}")
                print(f"     Classification: {classification}")

        print("\nRecommendation:")
        print(f"  {analysis['recommendation']}")

        print("=" * 60)

    def list_sources(self):
        """Return all information sources."""
        return self.sources
