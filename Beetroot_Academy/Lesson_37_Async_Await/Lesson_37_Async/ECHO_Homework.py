import asyncio


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    addr = writer.get_extra_info('peername')
    print(f'Новое подключение от {addr}')

    while True:
        data = await reader.read(1024)
        if not data:
            print(f'Клиент {addr} отключился')
            break

        message = data.decode().strip()
        print(f'Получено сообщение от {addr}: {message}')

        writer.write(data)
        await writer.drain()

    writer.close()
    await writer.wait_closed()
    print(f'Соединение с {addr} закрыто')


async def main() -> None:
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Сервер запущен на {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Сервер остановлен вручную')
