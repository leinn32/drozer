"""Utilities for reporting the success or failure of teams."""

from . import logger


def report_team_status(team_results):
    """Report team results to the drozer logger and return a summary string.

    Parameters
    ----------
    team_results : dict
        Mapping of team names to a boolean indicating success (True) or
        failure (False).

    Returns
    -------
    str
        A string summarising the team results in the form
        "<team>: SUCCESS" or "<team>: FAILURE" on separate lines.
    """
    lines = []
    for team, success in team_results.items():
        status = "SUCCESS" if success else "FAILURE"
        message = f"{team}: {status}"
        if success:
            logger.logger.info(message)
        else:
            logger.logger.warning(message)
        lines.append(message)
    return "\n".join(lines)
