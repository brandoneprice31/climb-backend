# climb-backend

## Endpoints

### POST /save_user_info
request:  
{  
  "first_name"  :   string,  
  "last_name"   :   string,  
  "fb_id"       :   string (optional),  
  "user_id"     :   string (optional, updates the user info if supplied)  
}  

response:  
{  
  "result"   :  {   "user_id"   :   string  }    
}  
