# climb-backend

## Endpoints

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


### POST /save_score
request:  
{  
&nbsp;&nbsp;"user_id"  :   string,  
&nbsp;&nbsp;"score"   :   int  
}  

response:  
{ }  


### POST /get_users_scores
request:  
{  
&nbsp;&nbsp;"user_id"  :   string,  
}  

response:  
{  
&nbsp;&nbsp;"result"   :  {   "scores"   :   [int]  }  
}  
