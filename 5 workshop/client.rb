#!/usr/bin/env ruby
require 'bunny'
require 'securerandom'

connection = Bunny.new(:host => '192.168.1.60', :user => 'jv', :password => 'h6gn5mvzx')
connection.start

channel = connection.create_channel
exchange = channel.fanout('')
queue_name = SecureRandom.uuid #=> "2d931510-d99f-494a-8c67-87feb05e1594"
queue = channel.queue(queue_name, exclusive: true)

def send_data(connection, exchange, queue_name = '')
	printf 'Input numbers x, y: '  
	STDOUT.flush  
	message = gets.chomp
  if message == ''
    puts 'Good bye'
    connection.close
    exit
  end
	exchange.publish(queue_name + ', ' + message, routing_key: '+')
	puts " [x] Sent #{message} q1"
end

send_data(connection, exchange, queue_name)
begin
  queue.subscribe(manual_ack: true, block: true) do |delivery_info, _properties, body|
    puts " [x] Received '#{body}'"
    # imitate some work
    sleep body.count('.').to_i
    channel.ack(delivery_info.delivery_tag)
    send_data(connection, exchange, queue_name)
  end
rescue Interrupt => _
  connection.close
end

