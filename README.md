# climb-backend

## Endpoints

===================
### POST /create_user
###### + Saves user information to the database.
request:
{
&nbsp;&nbsp;"first_name"  :   string,
&nbsp;&nbsp;"last_name"   :   string,
&nbsp;&nbsp;"fb_id"       :   string
}

response:
{  
&nbsp;&nbsp;"result" : {  
&nbsp;&nbsp;&nbsp;&nbsp;"user" : {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"fb_id" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"first_name" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"last_name" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"coins" : int,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"sprites" : {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"climber" : [int],  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"spikeball" : [int]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"extra_lives" : int,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"ads" : bool  
&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;}  
}  

===================
### POST /save_score
###### + Saves a new score to the database.
request:
{
&nbsp;&nbsp;"fb_id"  :   string,
&nbsp;&nbsp;"score"   :   int
}

response:
{ }

===================
### GET /get_users_scores
###### + Gets all of a user's scores from the database.
request:
{
&nbsp;&nbsp;"fb_id"  :   string,
}

response:
{
&nbsp;&nbsp;"result"   :  {   "scores"   :   [int]  }
}
