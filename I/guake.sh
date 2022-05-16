sudo apt install guake -y
guake
guake --restore-preferences=guake.default
dconf load / < guake.dconf
sudo rm -rf /usr/shar/applications/guake-prefs.desktop
echo done
