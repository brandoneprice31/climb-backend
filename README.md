# climb-backend

## Endpoints

### POST /save_user_info
request:  
{  
&nbsp;&nbsp;"first_name"  :   string,  
&nbsp;&nbsp;"last_name"   :   string,  
&nbsp;&nbsp;"fb_id"       :   string (optional),  
&nbsp;&nbsp;"user_id"     :   string (optional, updates the user info if supplied)  
}  

response:  
{  
&nbsp;&nbsp;"result"   :  {   "user_id"   :   string  }    
}  


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


### POST /get_global_scores
request:  
{ }  

response:  
{  
&nbsp;&nbsp;"result"   :  {   "scores"   :   [  
&nbsp;&nbsp;&nbsp;&nbsp;{ "first_name" : string, "last_name" : string, "score" : int}
&nbsp;&nbsp;]  }  
}  
