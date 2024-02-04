## Instructions
Install
```
sudo apt install ruby-full

# setup gems to work for non sudo
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

gem install jekyll bundler
bundle update github-pages
bundle add webrick
bundle install
```

Run Locally
```
bundle exec jekyll serve --livereload --trace
```

Deploy
```
Just push to the gh-pages branch :)
```


## TODO
devops
- [x] figure out how to build locally
- [x] deploy to github pages
- [x] hook up to domain name

blog
- [x] figure out how to edit template
- [x] edit nav bar
- [x] create separate category home pages (about, sw, hw, eship)
- [x] create css for circle images in previews
- [x] decide on design
- [x] copy in text and images from existing website
- [x] flesh out pictures and stuff for existing posts
- [x] cross post cobalt blog posts
- [ ] write up some recent cobalt projects!
    - [ ] docker on robots
    - [ ] if software were hardware
    - [ ] elevators
