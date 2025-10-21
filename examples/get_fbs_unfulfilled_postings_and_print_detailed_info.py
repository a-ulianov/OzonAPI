import asyncio
import datetime
from pprint import pprint

from src.ozonapi import SellerAPI, SellerAPIConfig
from src.ozonapi.seller.schemas.fbs import PostingFBSGetRequest, PostingFBSUnfulfilledListRequest, \
    PostingFBSUnfulfilledListFilter, PostingFBSGetResponse


async def get_fbs_unfulfilled_postings_and_print_detailed_info():
    """
    Получает и выводит детализированную информацию по каждому из необработанных FBS/rFBS отправлений за указанный
    период времени (последние 5 дней).
    """
    async with SellerAPI(
            # Понижаем уровень логирования для наглядности
            config=SellerAPIConfig(log_level="DEBUG")
    ) as api:
        # Параметры для выборки необработанных отправлений
        limit = 1000    # Определен в схеме запроса, здесь указан для наглядности
        offset = 0

        # Выбираем все необработанные отправления
        postings = list()
        while True:
            result = await api.posting_fbs_unfulfilled_list(
                PostingFBSUnfulfilledListRequest(
                    filter=PostingFBSUnfulfilledListFilter(
                        delivering_date_from=datetime.datetime.now() - datetime.timedelta(days=5),
                        delivering_date_to=datetime.datetime.now(),
                    ),
                    limit=limit,    # Максимум 1000, согласно документации PostingFBSUnfulfilledListRequest
                    offset=offset,  # Сдвиг выборки
                )
            )

            # Добавляем выбранные за одну итерацию данные в общий список
            postings.extend(result.result.postings)

            if len(postings) >= result.result.count:
                # Если выбрали всё, то выходим из цикла
                break
            else:
                # Увеличиваем сдвиг на limit
                offset += limit
            # Переходим к следующей итерации

        # Формируем список задач на параллельную выборку детализированной информации по каждому отправлению
        tasks = list()
        for posting in postings:
            tasks.append(
                await api.posting_fbs_get(
                    PostingFBSGetRequest(
                        posting_number=posting.posting_number
                    )
                )
            )

        # Выполняем все запросы параллельно (лимиты запросов сконфигурированы по умолчанию)
        detailed_postings: list[PostingFBSGetResponse] = await asyncio.gather(*tasks)

        # Выводим в консоль, предварительно преобразовав модели отправлений в словари (для наглядности)
        pprint([posting.model_dump() for posting in detailed_postings])

if __name__ == '__main__':
    asyncio.run(get_fbs_unfulfilled_postings_and_print_detailed_info())