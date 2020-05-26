Ripping Audio Streams from a DVD Into Separate MP3 Files
========================================================
I like live music, and one of the things I generally like to do is create
separate audio tracks from a concert video so that I can listen to them as I
would any other songs I have in my library. This guide and accompanying utility
program are how I create those tracks.

I'm assuming you're starting with a physical DVD. If you already have a readable
media file (either audio or video), you can skip to step 3.



1. Copy the dvd to your hard drive using the dvdbackup utility as follows

	dvdbackup -i /dev/sr0 -n Title_of_Your_DVD -o output_path -M -p
	
This copies the VOB files to output_path (-n forces the title, -M mirrors all
files, -p shows progress). This step can take a half hour or so. You can also
use Handbrake or whatever other software you prefer that can create a readable
video file.
 

2. Use ffmpeg to concatenate all the VOBs into a single file

	ffmpeg -i concat:"file1.vob|file2.vob|file3.vob" -c copy output.vob
	
3. Listen carefully to the resulting VOB file using a video viewer that has good
precise movement controls. I find the `mpv` player to be very good. Just use the
`O` option to show the elapsed time overlay as you're playing the file. You're
going to need to mark every track boundary by hand, so the ability to jump
forward and backward by coarse and fine increments is essential.

Note that you can use fractions of a second in the timestamps. This is useful
for a lot of concert DVDs that include tracks that spill into one another. 

As you go, you're building up a file that looks like this:

    track_number;track_name;artist_name;album_title;album_artist;year;start_time;end_time
	1;Uberesso;Sonny Landreth;Crossroads Guitar Festival 2007;Various Artists;2007;00:07:25.7;00:10:06
	2;Hell At Home; Sonny Landreth with Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;00:10:26;00:15:45
	3;Maharina;John McLaughlin;Crossroads Guitar Festival 2007;Various Artists;2007;00:17:26;00:24:44
	4;Rosie;Doyle Bramhall II;Crossroads Guitar Festival 2007;Various Artists;2007;00:26:10;00:32:19
	5;Outside Woman Blues;Doyle Bramhall II;Crossroads Guitar Festival 2007;Various Artists;2007;00:32:40;00:36:00
	6;Little By Little;Susan Tedeschi with the Derek Trucks Band;Crossroads Guitar Festival 2007;Various Artists;2007;00:37:35;00:42:52
	7;Anyday;The Derek Trucks Band;Crossroads Guitar Festival 2007;Various Artists;2007;00:43:10;00:49:25
	8;Highway 61 Revisited;Johnny Winter with the Derek Trucks Band;Crossroads Guitar Festival 2007;Various Artists;2007;00:50:20;00:58:16
	9;NobodySoul;Robert Randolph and the Family Band;Crossroads Guitar Festival 2007;Various Artists;2007;01:00:23;01:07:54
	10;Poor Johnny;Robert Cray;Crossroads Guitar Festival 2007;Various Artists;2007;01:09:09;01:15:02
	11;Dirty Work at the Crossroads;Jimmie Vaughan and the Robert Cray Band;Crossroads Guitar Festival 2007;Various Artists;2007;01:15:25;01:19:11
	12;Sittin on Top of the World;Hubert Sumlin with Robert Cray and Jimmie Vaughan;Crossroads Guitar Festival 2007;Various Artists;2007;01:20:49;01:25:08
	13;Paying the Cost to be the Boss;B.B. King with Robert Cray, Jimmie Vaughan, and Hubert Sumlin;Crossroads Guitar Festival 2007;Various Artists;2007;01:28:06;01:31:55
	14;Rock Me Baby;B.B. King with Robert Cray, Jimmie Vaughan, and Hubert Sumlin;Crossroads Guitar Festival 2007;Various Artists;2007;01:36:08;01:40:43
	15;Sweet Thing;Vince Gill;Crossroads Guitar Festival 2007;Various Artists;2007;01:42:46;01:47:39
	16;Country Boy;Albert Lee with Vince Gill;Crossroads Guitar Festival 2007;Various Artists;2007;01:48:03;01:52:42
	17;If it Makes You Happy;Sheryl Crow with Vince Gill and Albert Lee;Crossroads Guitar Festival 2007;Various Artists;2007;01:53:34;01:58:42
	18;Tulsa Time;Sheryl Crow with Eric Clapton, Vince Gill, and Albert Lee;Crossroads Guitar Festival 2007;Various Artists;2007;01:59:09;02:04:40
	19;Blue Eyes Crying in the Rain;Wille Nelson with Vince Gill and Albert Lee;Crossroads Guitar Festival 2007;Various Artists;2007;02:05:55;02:08:59
	20;On the Road Again;Willie Nelson with Sheryl Crow, Vince Gill, and Albert Lee;Crossroads Guitar Festival 2007;Various Artists;2007;02:09:29;02:11:40
	21;Belief;John Mayer;Crossroads Guitar Festival 2007;Various Artists;2007;02:14:42;02:20:32
	22;Gravity;John Mayer;Crossroads Guitar Festival 2007;Various Artists;2007;02:20:48;02:28:02
	23;Don't Worry Baby;Los Lobos;Crossroads Guitar Festival 2007;Various Artists;2007;02:30:00;02:33:02
	24;Mas y Mas;Los Lobos;Crossroads Guitar Festival 2007;Various Artists;2007;02:33:18;02:39:08
	25;Cause We've Ended as Lovers;Jeff Beck;Crossroads Guitar Festival 2007;Various Artists;2007;02:41:25;02:45:18
	26;Big Block;Jeff Beck;Crossroads Guitar Festival 2007;Various Artists;2007;02:45:43;02:51:08
	27;Tell the Truth;Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;02:54:35;03:01:46.5
	28;Little Queen of Spades;Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;03:01:46;03:14:30
	29;Isn't it a Pity;Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;03:15:01;03:21:03
	30;Who do you Love;Robbie Robertson with Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;03:22:11;03:26:27
	31;Presence of the Lord;Steve Winwood and Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;03:28:51;03:34:05
	32;Can't Find My Way Home;Steve Winwood and Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;03:34:34;03:39:26
	33;Had to Cry Today;Steve Winwood and Eric Clapton;Crossroads Guitar Festival 2007;Various Artists;2007;03:39:32;03:45:45
	34;Dear Mr. Fantasy;Steve Winwood;Crossroads Guitar Festival 2007;Various Artists;2007;03:45:54;03:54:00
	35;Crossroads;Eric Clapton and Steve Winwood;Crossroads Guitar Festival 2007;Various Artists;2007;03:54:20;03:59:49
	36;Mary Had a Little Lamb;Buddy Guy;Crossroads Guitar Festival 2007;Various Artists;2007;04:02:31;04:07:03.5
	37;Damn Right I've Got the Blues;Buddy Guy;Crossroads Guitar Festival 2007;Various Artists;2007;04:07:03.5;04:12:22
	38;Sweet Home Chicago;Buddy Guy with Eric Clapton, Robert Cray, John Mayer,	Hubert Sumlin, Jimmie Vaughan, and Johnny Winter;Crossroads Guitar Festival	2007;Various Artists;2007;04:12:33;04:19:40
	
This is basically a CSV but semicolon-delimited, purely just to make it slightly
more convenient to deal with since commas are more prevalent in song and artist
fields. Note the header row -- I like to include it as serves as a key of sorts,
but any line that doesn't start with a number will be skipped anyway. This can
be handy if something fails partway through. You can in that case "comment out"
tracks that have already been converted using any non-numeric value at the
beginning of the lines. 

Start and end times are always specified as hh:mm:ss[.s].

4. Once you're comfortable with this file, use the python program here to create
all the mp3s. The program also saves off flac files for each track. If you only
want the mp3s, you're free to delete the flac files after you're done.

	dvd2mp3.py source.vob tracklist.info [volume_boost]

If you don't specify a volume boost, you just get the default volume of the
media. I've found these can vary quite a lot though. If you have a source that's
too quiet, you can include a third argument that will be used as a scale factor
for the volume of the tracks. Specifying 1.0 would be unity boost. Values < 1.0
make the output quieter; greater than 1.0 make it louder. So

    dvd2mp3.py source.vob tracklist.info 1.5 

would result in each track being 50% louder than the source file. ffmpeg has
options to help you analyze the volume of a source file and do more elaborate
things, but I typically find it fine to just use the flat scaling of volume with
a bit of trial and error.
