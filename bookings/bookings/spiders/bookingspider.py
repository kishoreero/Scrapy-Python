import scrapy
from bookings.items import BookingsItem

class BookingspiderSpider(scrapy.Spider):
    name = 'bookingspider'
    
    start_urls = ['https://www.booking.com/hotel/in/residency-mumbai.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=24809401_91808653_0_1_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=6;highlighted_blocks=24809401_91808653_0_1_0;hpos=6;matching_block_id=24809401_91808653_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=24809401_91808653_0_1_0__451200;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/the-orchid-mumbai.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=26160710_350213067_2_42_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=7;highlighted_blocks=26160710_350213067_2_42_0;hpos=7;matching_block_id=26160710_350213067_2_42_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=26160710_350213067_2_42_0__664924;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/jw-marriott-mumbai-sahar.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=130073609_130684979_0_42_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=8;highlighted_blocks=130073609_130684979_0_42_0;hpos=8;matching_block_id=130073609_130684979_0_42_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=130073609_130684979_0_42_0__850000;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/courtyard-by-marriott-mumbai-international-airport.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=23899903_150070089_2_2_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=10;highlighted_blocks=23899903_150070089_2_2_0;hpos=10;matching_block_id=23899903_150070089_2_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=23899903_150070089_2_2_0__650000;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/itc-maratha-mumbai.html?label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=838e8c4dc88d5cbc62aae2c3ce267a4f&aid=304142&ucfs=1&arphpl=1&checkin=2022-08-18&checkout=2022-08-19&dest_id=-2092174&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=612a4bc6e1980016&srepoch=1660214798&all_sr_blocks=47077314_244938433_0_40_0&highlighted_blocks=47077314_244938433_0_40_0&matching_block_id=47077314_244938433_0_40_0&sr_pri_blocks=47077314_244938433_0_40_0__850000&from_beach_sr=1&from_sustainable_property_sr=1&from=searchresults#hotelTmpl','https://www.booking.com/hotel/in/sofitel-mumbai-bkc.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=29408601_94398659_2_1_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=13;highlighted_blocks=29408601_94398659_2_1_0;hpos=13;matching_block_id=29408601_94398659_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=29408601_94398659_2_1_0__850000;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/the-leela-mumbai.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=24995101_278096417_2_42_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=14;highlighted_blocks=24995101_278096417_2_42_0;hpos=14;matching_block_id=24995101_278096417_2_42_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=24995101_278096417_2_42_0__1000000;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/taj-president.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=7473606_218722826_2_2_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=19;highlighted_blocks=7473606_218722826_2_2_0;hpos=19;matching_block_id=7473606_218722826_2_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=7473606_218722826_2_2_0__1000000;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/hilton-mumbai-international-airport.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=28362407_266007748_2_42_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=21;highlighted_blocks=28362407_266007748_2_42_0;hpos=21;matching_block_id=28362407_266007748_2_42_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=28362407_266007748_2_42_0__900000;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/bawa-international.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=24452610_355860423_2_0_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=23;highlighted_blocks=24452610_355860423_2_0_0;hpos=23;matching_block_id=24452610_355860423_2_0_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=24452610_355860423_2_0_0__500000;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl','https://www.booking.com/hotel/in/royal-hometel-suites.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4As2705cGwAIB0gIkNzZiYjExMTMtYzZiYS00OGQ5LTg1NjMtNzg4YTYwMTQzZjFk2AIF4AIB&sid=7e0e329636b233f896e102f58dea208f&all_sr_blocks=560352201_270500605_2_42_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2092174;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=25;highlighted_blocks=560352201_270500605_2_42_0;hpos=25;matching_block_id=560352201_270500605_2_42_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=560352201_270500605_2_42_0__409900;srepoch=1660214798;srpvid=612a4bc6e1980016;type=total;ucfs=1&#hotelTmpl']
    
    def parse(self, response):
        booking_hotel = BookingsItem()
       
        booking_hotel['name']=response.css('h2[id="hp_hotel_name"]::text').extract()
        booking_hotel['address'] = response.xpath("//*[@id='showMap2']/span[1]/text()").extract_first().strip()
        booking_hotel['rating'] = response.xpath("//*[@id='review_list_score']/div[1]/span/span[1]/text()").extract_first().strip()
        booking_hotel['property_description'] = response.css('div[id="property_description_content"] p::text').getall()
        booking_hotel['rating_count'] = response.css('li[class="hp_nav_bar_item"] span::text').extract()[1]
        booking_hotel['breakfast_type'] = response.xpath("//*[@id='basiclayout']/div[1]/div/div[5]/div/div/div[2]/div/div[1]/div[2]/div[2]/p/span/span/text()").getall()
        booking_hotel['parking'] = response.css('span[class="ph-item-copy-parking"]::text').getall()
        booking_hotel['rating_type'] = response.xpath("//*[@id='review_list_score']/div[1]/span/span[2]/span[1]/text()").extract_first().strip()
        booking_hotel['pets'] = response.xpath("//*[@id='hotelPoliciesInc']/div[6]/p[2]/text()").extract()[0]
	
        yield booking_hotel
		  


