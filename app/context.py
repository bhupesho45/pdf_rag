def build_context(results):
    context_parts = []

    for result in results:
        chunk = result["chunk"]

        context_parts.append(
            f"Page {chunk['page']}:\n{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    return context
