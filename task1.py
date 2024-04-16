from datetime import datetime

def get_days_from_today(date: str) ->int:
    """
    This function calculates days between passed date and today.
    The input date should be in format 'YYYY-MM-DD'.
    Function ignores time part of the date
    Returns days between dates as integer value or error if string to datetime conversion fails.
    """

    try:
        input_date=datetime.strptime(date,"%Y-%m-%d").date()  #trying to convert string representation of date to the datetime object
    except (TypeError, ValueError):
        return f"the entered date '{date}' is incorrect. Please try to enter again in the correct format 'YYYY-MM-DD'" #Return error message
        
    
    current_date=datetime.now().date() # Get current date

    return (input_date - current_date).days