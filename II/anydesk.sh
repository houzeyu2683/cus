#wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -
#sudo sh -c 'echo "deb http://deb.anydesk.com/ all main" > /etc/apt/sources.list.d/anydesk-stable.list'
file="anydesk_6.1.1-1_amd64.deb"
url="https://download.anydesk.com/linux/"
link="$url$file"
wget $link
sudo dpkg -i $file
rm $file
echo done
#sudo apt update
#sudo apt install anydesk -y
#echo done
