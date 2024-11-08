from docling.document_converter import DocumentConverter

def convert_document(source):
    """
    Converts a document from a given source (file path or URL) to markdown format.

    Args:
        source (str): The path or URL of the document to be converted.

    Returns:
        str: The converted document content in markdown format.
    """
    # Create a DocumentConverter instance
    converter = DocumentConverter()
    # Convert the document from the source
    result = converter.convert(source)
    # Export the result to markdown
    return result.document.export_to_markdown() 