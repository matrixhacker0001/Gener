# Gener
A tool to print list of hex codes..

** Created By - M4trix_h4ck3r

## Usage:

> To print help banner of program

```
C:\Python27>python.exe C:\users\m4trix\desktop\gener.py help
                     ,;L.                     ,;
         .Gt       f#i EW:        ,ft       f#i j.
        j#W:     .E#t  E##;       t#E     .E#t  EW,
      ;K#f      i#W,   E###t      t#E    i#W,   E##j
    .G#D.      L#D.    E#fE#f     t#E   L#D.    E###D.
   j#K;      :K#Wfff;  E#t D#G    t#E :K#Wfff;  E#jG#W;
 ,K#f   ,GD; i##WLLLLt E#t  f#E.  t#E i##WLLLLt E#t t##f
  j#Wi   E#t  .E#L     E#t   t#K: t#E  .E#L     E#t  :K#E:
   .G#D: E#t    f#E:   E#t    ;#W,t#E    f#E:   E#KDDDD###i
     ,K#fK#t     ,WW;  E#t     :K#D#E     ,WW;  E#f,t#Wi,,,
       j###t      .D#; E#t      .E##E      .D#; E#t  ;#W:
        .G#t        tt ..         G#E        tt DWi   ,KK:
          ;;                       fE
                                    ,

------------------------------------------------------------

 A Hex Character List Generation tool
 ===========================================
 Usage: ./gener.py [options]

 all - print complete list with all hex values
 {badchar} - badchar to remove. Format [\x00][00][x00]
 help - show this banner

```


> To print complete list of hex values without badchar

```
C:\Python27>python.exe C:\users\m4trix\desktop\gener.py all
                     ,;L.                     ,;
         .Gt       f#i EW:        ,ft       f#i j.
        j#W:     .E#t  E##;       t#E     .E#t  EW,
      ;K#f      i#W,   E###t      t#E    i#W,   E##j
    .G#D.      L#D.    E#fE#f     t#E   L#D.    E###D.
   j#K;      :K#Wfff;  E#t D#G    t#E :K#Wfff;  E#jG#W;
 ,K#f   ,GD; i##WLLLLt E#t  f#E.  t#E i##WLLLLt E#t t##f
  j#Wi   E#t  .E#L     E#t   t#K: t#E  .E#L     E#t  :K#E:
   .G#D: E#t    f#E:   E#t    ;#W,t#E    f#E:   E#KDDDD###i
     ,K#fK#t     ,WW;  E#t     :K#D#E     ,WW;  E#f,t#Wi,,,
       j###t      .D#; E#t      .E##E      .D#; E#t  ;#W:
        .G#t        tt ..         G#E        tt DWi   ,KK:
          ;;                       fE
                                    ,

------------------------------------------------------------

\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f
\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f
\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f
\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f
\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f
\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f
\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f
\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f
\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f
\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f
\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf
\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf
\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf
\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf
\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef
\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff

```


> To print list of hex values and remove bad chars from it..

Bad char format :
- \x0a,\x00
- x0a,x00
- 0a,00

```
C:\Python27>python.exe C:\users\m4trix\desktop\gener.py \x00,\x0a
                     ,;L.                     ,;
         .Gt       f#i EW:        ,ft       f#i j.
        j#W:     .E#t  E##;       t#E     .E#t  EW,
      ;K#f      i#W,   E###t      t#E    i#W,   E##j
    .G#D.      L#D.    E#fE#f     t#E   L#D.    E###D.
   j#K;      :K#Wfff;  E#t D#G    t#E :K#Wfff;  E#jG#W;
 ,K#f   ,GD; i##WLLLLt E#t  f#E.  t#E i##WLLLLt E#t t##f
  j#Wi   E#t  .E#L     E#t   t#K: t#E  .E#L     E#t  :K#E:
   .G#D: E#t    f#E:   E#t    ;#W,t#E    f#E:   E#KDDDD###i
     ,K#fK#t     ,WW;  E#t     :K#D#E     ,WW;  E#f,t#Wi,,,
       j###t      .D#; E#t      .E##E      .D#; E#t  ;#W:
        .G#t        tt ..         G#E        tt DWi   ,KK:
          ;;                       fE
                                    ,

------------------------------------------------------------

\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f
\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f
\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f
\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f
\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f
\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f
\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f
\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f
\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f
\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f
\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf
\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf
\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf
\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf
\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef
\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff

```
