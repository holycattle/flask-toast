#-*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  module_path = ["puppet/modules", "puppet/vendor_modules"]

  config.vm.box = "ubuntu-precise-32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"
  config.vm.customize ["modifyvm", :id, "--memory", 128]
  config.vm.share_folder "angular-momentum", "/home/vagrant/flask-toast", ".", :nfs => true
  config.vm.share_folder "angular-momentum-nginx", "/var/www/flask-toast", ".", :nfs => true
  config.vm.network :hostonly, "172.16.0.41"
  config.vm.forward_port 80, 8000
  config.vm.provision :puppet, :module_path => module_path do |puppet|
    puppet.manifests_path = "puppet"
    puppet.manifest_file  = "flask-toast.pp"
  end
  config.vm.host_name = "flask-toast"
end