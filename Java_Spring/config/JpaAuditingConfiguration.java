import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@Configuration
@EnableJpaAuditing
// 설정해줌으로써 자동으로 생성일과 수정일을 관리해준다.
public class JpaAuditingConfiguration {
}
