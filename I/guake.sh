sudo apt install guake -y
sudo rm -rf /usr/shar/applications/guake-prefs.desktop
guake --restore-preferences=guake.default
dconf load / < guake.dconf
echo done
