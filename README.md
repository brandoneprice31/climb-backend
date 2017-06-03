# climb-backend

## Endpoints

### POST /save_user_info
request:\n
{\n
  "first_name"  :   string,\n
  "last_name"   :   string,\n
  "fb_id"       :   string (optional),\n
  "user_id"     :   string (optional, updates the user info)\n
}\n

response:
{
  "result"   :
    {
      "user_id"   :   string
    }
}
