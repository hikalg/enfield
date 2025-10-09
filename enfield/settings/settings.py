class BasicSettings():
    
    organisation_name : str = "organisation"
    
class TeamSettings():
    
    team_default_name : str = "placeholder"
    
    minimum_team_size : int = 0
    maximum_team_size : int = 5
    
class RatingSettings():
    
    '''
    Minimum and maximum ratings should be 10x apart.
    '''
    minimum_rating : int = 500
    maximum_rating : int = 5000
    
    default_scaling : float = 1.00
    
class MatchSettings():
    
    minimum_team_size : int = TeamSettings().minimum_team_size
    
    maximum_team_size : int = TeamSettings().maximum_team_size