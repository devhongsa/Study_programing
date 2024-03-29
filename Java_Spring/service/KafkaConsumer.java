import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class KafkaConsumer {

    private static final String TOPIC_NAME = "topic5";

    ObjectMapper objectMapper = new ObjectMapper();

    @KafkaListener(topics = TOPIC_NAME)
    public void listenMessage(String jsonMessage) {
        try {
            MyMessage message = objectMapper.readValue(jsonMessage, MyMessage.class);
            System.out.println(">>>" + message.getName() + "," + message.getMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// 이것만 만들어놔도 이 어플리케이션에서 메세지를 자동으로 수신함.