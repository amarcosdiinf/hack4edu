class Account:
   
    @staticmethod
    def from_instagram(insta_account):
        account = Account(
            insta_account.identifier,
            insta_account.username,
            insta_account.full_name,
            insta_account.biography,
            insta_account.profile_pic_url_hd,
            insta_account.media_count,
            insta_account.followed_by_count,
            insta_account.follows_count,
            insta_account.is_verified
        )
        return account
        
    @staticmethod
    def from_twitter(self, insta_account):
        """self.acc_id = insta_account.identifier
        self.username = insta_account.username
        self.full_name = insta_account.full_name
        self.biography = insta_account.biography
        self.profile_image_url = insta_account.profile_pic_url_hd
        self.n_post = insta_account.media_count
        self.n_followers = insta_account.followed_by_count
        self.n_follows = insta_account.follows_count
        self.verified = insta_account.is_verified
        self.location = None"""

        
     
    def __init__(self, acc_id, username, full_name, biography, profile_image_url, n_post, n_followers, n_follows, verified, location = None):
        self.acc_id = acc_id
        self.username = username
        self.full_name = full_name
        self.biography = biography
        self.profile_image_url = profile_image_url
        self.n_post = n_post
        self.n_followers = n_followers
        self.n_follows = n_follows
        self.verified = verified
        self.location = location