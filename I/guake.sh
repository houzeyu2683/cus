sudo apt install guake -y
guake --restore-preferences=guake.default
dconf load / < guake.dconf
sudo rm -rf /usr/share/applications/guake-prefs.desktop
guake &
echo done
