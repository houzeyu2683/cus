sudo add-apt-repository ppa:linuxuprising/guake
sudo apt update
sudo apt install guake -y
# mkdir -p ~/.config/autostart/
sudo cp /usr/share/guake/autostart-guake.desktop /etc/xdg/autostart/
# sudo cp /usr/share/applications/guake.desktop /etc/xdg/autostart/
dconf load / < guake.dconf
echo done
