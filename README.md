# Tweet archiver #

These Python scripts and the related files will download your tweets, mentions, favorites and direct messages from Twitter and save them in a plaintext archive file on your computer. It is intended to be run periodically to add recent tweets to an existing archive file. The original script (in a slightly earlier version, only for archiving tweets) is described in [this blog post][1]. If you already have an archive of tweets in ThinkUp, you might find [this post][2] useful in turning it into a plaintext archive. If you are starting an archive from scratch, [this post and script][3] by Tim Bueno will be helpful.

The files in the repository are:

* A collection of scripts that perform the archiving, which can be be stored anywhere and should be run periodically via a system like `cron` or `launchd`.
	- `archive-tweets.py`: archives tweets to `tweets.txt`.
	- `archive-mentions.py`: archives mentions to `mentions.txt`.
	- `archive-faves`: archives favorites to `favorites.txt`.
	- `archive-dm-received`: archives direct messages received from other users to `dmessages-received.txt`.
	- `archive-dm-sent`: archives direct messages sent to other users to `dmessages-sent.txt`.
* `tweets.txt`, `mentions.txt`, `favorites.txt`, `dmessages-received`, `dmessages-sent`. These are the archive files themselves, currently empty. They should be kept in a folder named `twitter` inside your Dropbox folder.
* `twitter-credentials`. This file should be renamed `.twitter-credentials` and saved in your home directory. The values for `consumerKey`, `consumerSecret`, `token`, and `tokenSecret` must be provided by Twitter. Go to the [Twitter developer site][4], click the "Create an app" link, and follow the instructions given there for creating an app. When you're done, you'll be given the four credentials—long strings of letters and numbers—you'll need. If you want to archive your direct messages, you'll also need to allow your app to "read, write and access direct messages" (configured in the "Settings" tab).
* `lastID.txt`. This file holds the ID numbers of the most recently archived tweet, mention, favorite, etc.; it currently holds dummy values you'll need to change. It should be kept in the same folder as the archive files.

You don't *have* to keep your archive in Dropbox, but that's a convenient place to be able to access your tweets from any of your computers. The directory for the archive can be changed by editing Line 10 of `archive-$entity.py`.

You also don't *have* to archive every type of message, and you can delete the associated script and empty archive file if you want. However, keep the dummy values in `lastID.txt` unless you edit Line 62 of the remaining scripts, which updates the value in `lastID.txt`.


[1]: http://www.leancrew.com/all-this/2012/07/archiving-tweets-without-ifttt/
[2]: http://www.leancrew.com/all-this/2012/07/archiving-tweets/
[3]: http://www.timbueno.com/2012/07/07/rolling-my-own-automatic-tweet-archiver
[4]: https://dev.twitter.com/