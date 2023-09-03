//J- Define the websocket server?
WebsocketServer::WebsocketServer(const std::string &host) : server(std::make_unique<ix::WebSocketServer>(42000, host)) {
	server->setOnConnectionCallback([this](std::weak_ptr<ix::WebSocket> webSocket, std::shared_ptr<ix::ConnectionState> connectionState) {
		//std::cout << "Remote ip: " << connectionState->remoteIp << std::endl;
		auto ws = webSocket.lock();
		if (ws) {
			ws->setOnMessageCallback([webSocket, connectionState, this](const ix::WebSocketMessagePtr &msg) {
				if (msg->type == ix::WebSocketMessageType::Open) {
					logger.WriteDebug("New connection");

					// A connection state object is available, and has a default id
					// You can subclass ConnectionState and pass an alternate factory
					// to override it. It is useful if you want to store custom
					// attributes per connection (authenticated bool flag, attributes, etc...)
					logger.WriteDebug("id: ", connectionState->getId());

					// The uri the client did connect to.
					logger.WriteDebug("Uri: ", msg->openInfo.uri);

					logger.WriteDebug("Headers:");
					for (auto it : msg->openInfo.headers) {
						logger.WriteDebug(it.first, ": ", it.second);
					}

					clients.emplace(std::make_pair(connectionState->getId(), webSocket));

					if (onOpen)
						onOpen(connectionState->getId());
				} else if (msg->type == ix::WebSocketMessageType::Message) {

					if (onMessage)
						onMessage(connectionState->getId(), msg->str, msg->binary);
				} else if (msg->type == ix::WebSocketMessageType::Close) {
					if (onDisconnect)
						onDisconnect(connectionState->getId());

					if (auto iter = clients.find(connectionState->getId()); iter != clients.end()) {
						auto ws = webSocket.lock();
						if (ws)
							ws->setOnMessageCallback(nullptr);
						clients.erase(iter);
					}
				}
			});
		}
	});
}