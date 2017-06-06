# climb-backend TODO ENPOINTS

## Endpoints TODO

===================
### GET /check_fb_id
###### + returns true if fb_id already in the database

===================
(NOTE: rename the save_user_info path you created to save_user_id. This endpoint
is more aptly named save_user_info.)

### POST /save_user_info (rename the other to save_user_id)
###### + saves the user's amount of coins, the climber sprites they have
unlocked, the spikeball sprites they have unlocked, which climber sprite is
chosen (lowercase string of the color) and which spikeball sprite is chosen
(string). The sprite unlock info should be a dictionary of [String : Bool],
where the string is the color (see the UserDefaults I setup in
GameViewController for reference to all these).

===================
### GET /get_user_info
###### + gets the user's info described above

===================
### GET /get_friends_scores
###### + given user's fb_id, gets the user's friends' best scores returning a
list of dictionaries of {first_name, last_name, score}

===================
### GET /get_global_scores
###### + gets the top 100 global scores {first_name, last_name, score}. This
does not have to be only best scores (one person can have multiple spots)



## Additional Endpoints for ad functionality

===================
### UPDATE: (currently save_user_info, but please rename to: ) save_user_id

###### + just add a boolean called no_ads that is initiated as false when a
user's info is saved (I am going to make it so that save_user_info is called
only when a user logs into the game for the first time)

===================
### POST: /update_ad_status
###### + make this so that I can toggle a user's ads boolean to false after a
purchase

===================
### GET /check_ad_status
###### + returns the no_ads boolean status
