



### Install and setup zsh

```bash
    sudo apt update
    sudo apt upgrade

    # install zsh
    sudo apt install zsh
    chsh -s /bin/zsh

    # reload the terminal (logoff / login)

    # Get ohmyzsh
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

    # Install MesloLGS NF Font and change the terminal profile to use this font
    # https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf

    # setup powerlevel10k
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"

    # set ZSH_THEME to be powerlevel10k in .zshrc
    # ZSH_THEME="powerlevel10k/powerlevel10k"
    vim ~/.zshrc
```

### Customizing ls output to fix weird formatting

#### 🔍 What Do the Keys Mean?

Key	Meaning
di	Directory
ln	Symbolic link
mh	Multi-hardlink
pi	Named pipe (FIFO)
so	Socket
do	Door (mostly Solaris)
bd	Block device
cd	Character device
or	Broken symlink
su	Setuid executable
sg	Setgid executable
tw	Sticky and writable dir
ow	Other writable dir (no sticky)
st	Sticky dir (not writable)
ex	Executable file
*.ext	Specific file extensions

#### 🎨 ANSI Color Code Format
The format is:

```css
    [attribute];[foreground];[background]
    Attributes:
    00 = default
    01 = bold

    
    Colors (foreground / background):
    Black: 30 / 40
    Red: 31 / 41
    Green: 32 / 42
    Yellow: 33 / 43
    Blue: 34 / 44
    Magenta: 35 / 45
    Cyan: 36 / 46
    White: 37 / 47
    

    So di=1;36;44 means:
    Bold (1)
    Cyan text (36)
    Blue background (44) → which is what you found hard to read.
```

#### Dark Mode

```bash
    di=01;34         # directories: bold blue
    ln=01;36         # symlinks: bold cyan
    pi=33            # named pipe: yellow
    so=35            # socket: magenta
    do=35            # door: magenta (if used)
    bd=01;33         # block device: bold yellow
    cd=01;33         # char device: bold yellow
    or=01;31         # broken symlink: bold red
    su=01;37;41      # setuid: bold white on red
    sg=01;30;43      # setgid: bold black on yellow
    tw=30;42         # sticky+writable: black on green
    ow=34;42         # other-writable: blue on green
    st=37;44         # sticky: white on blue
    ex=01;32         # executable: bold green
    Note:

    Removed harsh backgrounds from directories.

    Used bold colors only where useful.

    Backgrounds are reserved for special permissions or flags.
```

```bash
    export LS_COLORS='di=01;34:ln=01;36:pi=33:so=35:do=35:bd=01;33:cd=01;33:or=01;31:su=01;37;41:sg=01;30;43:tw=30;42:ow=34;42:st=37;44:ex=01;32'
    source ~/.bashrc   # or ~/.zshrc
```















