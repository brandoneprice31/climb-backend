# climb-backend

## Endpoints

===================
### POST /save_user_info
###### + Saves / updates user information to the database.
request:  
{  
&nbsp;&nbsp;"first_name"  :   string,  
&nbsp;&nbsp;"last_name"   :   string,  
&nbsp;&nbsp;"fb_id"       :   string  
}  

response:  
{ }  

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
### POST /get_users_scores
###### + Gets all of a user's scores from the database.
request:  
{  
&nbsp;&nbsp;"fb_id"  :   string,  
}  

response:  
{  
&nbsp;&nbsp;"result"   :  {   "scores"   :   [int]  }  
}  
