# climb-backend TODO ENPOINTS

## Endpoints TODO

===================
### GET /check_fb_id
###### + returns true if fb_id already in the database

===================
*UPDATE OF CURRENT ENDPOINT*
### POST /create_user
(NOTE: this is an edit of the current save_user_info path. Please re-write that
path with the new name and the following info)
###### + this will initiate a user's information. Their fb_id, first name, last
name will all be saved. The database will also create default values for in-game
stats. This includes: the amount of coins the user has (0), the climber sprites
unlocked, the spikeball sprites unlocked, which climber sprite is currently
chosen, which spikeball spite is currently chosen, and how many extra lives they
have (0), and a boolean called ads initiated as true. These default values are
set in the GameViewController right now as UserDefaults. Look at the initial
values I create there to see what these initial values should be.

### POST /save_user_info (rename the other to create_user)
###### + saves the user's amount of coins, the climber sprites they have
unlocked, the spikeball sprites they have unlocked, which climber sprite is
chosen (lowercase string of the color), which spikeball sprite is chosen,
how many extra lives they have, and the ads boolean. The sprite unlock info
should be a dictionary of [String : Bool], where the string is the color (see
the UserDefaults I setup in GameViewController for reference to all these).

===================
### GET /get_user_info
###### + gets the user's info described above

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
