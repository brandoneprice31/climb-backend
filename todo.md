# climb-backend TODO ENPOINTS

## Endpoints TODO

===================
### GET /check_fb_id
###### + returns true if fb_id already in the database

===================
*UPDATE OF CURRENT ENDPOINT*
### POST /save_user_info (rename the other to create_user)
###### + saves the user's amount of coins, the climber sprites they have
unlocked, the spikeball sprites they have unlocked, which climber sprite is
chosen (lowercase string of the color), which spikeball sprite is chosen,
how many extra lives they have, and the ads boolean. The sprite unlock info
should be a dictionary of [String : Bool], where the string is the color (see
the UserDefaults I setup in GameViewController for reference to all these).

===================
### POST /update_user_info
###### + given a fb_id, I want to be able to update the coins, climber sprites,
spikeball sprites, current climber, current spikeball, extra lives, and ads
categories. We don't need to touch the name fields.

===================
### GET /get_friends_scores
###### + given user's fb_id, gets the user's friends' best scores returning a
list of dictionaries of {first_name, last_name, score}

===================
### GET /get_global_scores
###### + gets the top 100 global scores {first_name, last_name, score}. This
does not have to be only best scores (one person can have multiple spots)

===================
### GET /get_rank
###### + given user fb_id, displays player rank globally
