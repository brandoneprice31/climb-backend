# climb-backend

## Endpoints

===================
### POST /create_user
###### + Creates a new user.
**request:**
{  
&nbsp;&nbsp;"first_name"  :   string,  
&nbsp;&nbsp;"last_name"   :   string,  
&nbsp;&nbsp;"fb_id"       :   string  
}  

**response:**
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
### POST /get_user_info
###### + Gets the user's info from the database.
**request:**
{  
&nbsp;&nbsp;"fb_id"  :   string  
}  

**response:**
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
### POST /save_user_info
###### + Updates the user info in the database.
**request:**
{
&nbsp;&nbsp;"fb_id"  :   string  
&nbsp;&nbsp;"sprites" (optional) :   {  
&nbsp;&nbsp;&nbsp;&nbsp;"climber" : [int],  
&nbsp;&nbsp;&nbsp;&nbsp;"spikeball" : [int],  
&nbsp;&nbsp;},  
&nbsp;&nbsp;"ads" (optional) : bool,  
&nbsp;&nbsp;"extra_lives" (optional) : int,  
&nbsp;&nbsp;"coins" (optional) : int  
}

**response:**
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
**request:**
{  
&nbsp;&nbsp;"fb_id"  :   string,  
&nbsp;&nbsp;"score"   :   int  
}  

**response:**
{ }  

===================
### POST /get_users_scores
###### + Gets all of a user's scores from the database.
**request:**
{  
&nbsp;&nbsp;"fb_id"  :   string,  
}  

**response:**
{  
&nbsp;&nbsp;"result"   :  {   "scores"   :   [int]  }  
}  

===================
### POST /get_friends_scores
###### + Gets all of the scores from a list of id's.
**request:**
{  
&nbsp;&nbsp;"friend_ids" : [string]  
}  

**response:**
{  
&nbsp;&nbsp;"result" : {  
&nbsp;&nbsp;&nbsp;&nbsp;"scores" : [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"first_name" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"last_name" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"fb_id" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"score" : int  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;]  
&nbsp;&nbsp;}  
}  

===================
### GET /get_global_scores
###### + Gets the top 100 scores.

**response:**
{  
&nbsp;&nbsp;"result" : {  
&nbsp;&nbsp;&nbsp;&nbsp;"scores" : [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"first_name" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"last_name" : string,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"score" : int  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  
&nbsp;&nbsp;&nbsp;&nbsp;]  
&nbsp;&nbsp;}  
}  

===================
### POST /get_rank
###### + Gets the user's global rank.
**request:**
{  
&nbsp;&nbsp;"fb_id" : string  
}  

**response:**
{  
&nbsp;&nbsp;"result" : {  
&nbsp;&nbsp;&nbsp;&nbsp;"rank" : int  
&nbsp;&nbsp;}  
}  
