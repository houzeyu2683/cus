sudo apt install guake -y
#guake --restore-preferences=guake.default
#cat guake.kshortcutsrc >> ~/.config/kglobalshortcutsrc
dconf load / < guake.dconf
sudo rm -rf /usr/share/applications/guake-prefs.desktop
sudo rm -rf /usr/share/applications/guake.desktop
#guake &
echo done

