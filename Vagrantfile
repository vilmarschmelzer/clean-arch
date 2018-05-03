# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'fileutils'

if File.directory?('.git')
    FileUtils.mkpath 'public'
end

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"
  config.vm.provider "libvirt"
  config.vm.provider "virtualbox"

  config.vm.synced_folder "./public", "/vagrant", type: "nfs", nfs_udp: false
  config.vm.synced_folder "~/git", "/git", type: "nfs", nfs_udp: false

  config.vm.provider :libvirt do |libvirt|
    libvirt.memory = 2048
  end

  config.vm.network :public_network,
      :dev => "virbr0",
      :mode => "bridge",
      :type => "bridge"
end
