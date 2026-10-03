import requests as req

def check_status(url: str) -> int:
    """This method checks status of the webiste
    
    Parameters
    ----------
    url: str
        url of the website to check

    Returns
    -------
    The status code of the website
    """
    req_check = req.get(url)

    if req_check.status_code == 200:
        return 200
    else:
        return 400



