import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.kstream.Grouped;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.Produced;
import org.apache.kafka.streams.kstream.TimeWindows;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import java.time.Duration;

@Component
public class StreamListener {

    @Bean
    public KStream<String, String> kStream(StreamsBuilder builder) {
        final String inputTopic = "checkout.complete.v1";  // 이 토픽에서 메세지 consumer
        final String outputTopic = "checkout.productId.aggregated.v1"; // 이 토픽으로 메세지 produce

        KStream<String, String> inputStream = builder.stream(inputTopic);
        inputStream
                // key,value 설정 
                .map((k, v) -> new KeyValue<>(JsonUtils.getProductId(v), JsonUtils.getAmount(v)))
                // Group by productId, key로 그룹핑 
                .groupByKey(Grouped.with(Serdes.Long(), Serdes.Long()))
                // Window 설정, 지난 1분간의 데이터를 가지고 그룹핑
                .windowedBy(TimeWindows.of(Duration.ofMinutes(1)))
                // Apply sum method, value에 대한 합
                .reduce(Long::sum)
                // map the window key
                .toStream((key, value) -> key.key())
                // outputTopic 에 보낼 Json String 으로 Generate
                .mapValues(JsonUtils::getSendingJson)
                // outputTopic 으로 보낼 key 값을 null 설정
                .selectKey((key, value) -> null)
                // outputTopic 으로 메세지(null, jsonString) 전송 설정
                .to(outputTopic, Produced.with(null, Serdes.String()));

        return inputStream;
    }
}