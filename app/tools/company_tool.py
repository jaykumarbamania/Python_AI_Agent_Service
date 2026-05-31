from langchain_core.tools import tool


@tool
def get_company_name():
    """
    Returns company name
    """

    return "Jay OMS Pvt Ltd"