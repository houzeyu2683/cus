file="code_1.56.2-1620838498_amd64.deb"
url="https://az764295.vo.msecnd.net/stable/054a9295330880ed74ceaedda236253b4f39a335/"
link="$url$file"
wget $link
sudo dpkg -i $file
rm $file
echo done
