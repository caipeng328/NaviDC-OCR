git config --global user.name "caipeng328"
git config --global user.email "lntu_caipeng@163.com"
ls ~/.ssh

ssh-keygen -t ed25519 -C "lntu_caipeng@163.com"
    ~/.ssh/id_ed25519
    ~/.ssh/id_ed25519.pub
cat ~/.ssh/id_ed25519.pub
    添加密钥

git remote add origin git@github.com:caipeng328/StarAGI-OCR.git
git branch -M main
git push -u origin main