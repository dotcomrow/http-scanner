def process(texts, settings):
    # Placeholder idea extractor
    results = []
    for text in texts:
        findings = {
            "original": text[:500],
            "findings": ["[Sample] Idea: Improve UX", "[Sample] Complaint: Too slow loading"],
        }
        results.append(findings)
    return results
