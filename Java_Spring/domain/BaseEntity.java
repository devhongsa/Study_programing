import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.datatype.jsr310.deser.LocalDateTimeDeserializer;
import com.fasterxml.jackson.datatype.jsr310.ser.LocalDateTimeSerializer;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.EntityListeners;
import javax.persistence.MappedSuperclass;
import java.time.LocalDateTime;

/*
    모든 엔티티에 적용할 base 컬럼
 */
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public class BaseEntity {
    @JsonSerialize(using = LocalDateTimeSerializer.class)
    @JsonDeserialize(using = LocalDateTimeDeserializer.class)
    @CreatedDate
    private LocalDateTime createdAt;

    @JsonSerialize(using = LocalDateTimeSerializer.class)
    @JsonDeserialize(using = LocalDateTimeDeserializer.class)
    @LastModifiedDate
    private LocalDateTime modifiedAt;
}

// config 에서 JpaAuditingConfiguration 설정해줘야한다.
// @EnableJpaAuditing을 설정해줌으로써 자동으로 생성일과 수정일을 관리해준다.

// @Column : name, length, nullable, unique
// @Column(columnDefinition = "TEXT")
// @Id
// @GeneratedValue : strategy = GenerationType.IDENTITY
// @Transient : 데이터베이스에 저장하지 않을 컬럼.
// @Enumerated : EnumType.STRING, ORDINALㄴ
// @Table
// @JoinColumn : FK 지정 관련
// @OneToOne, OneToMany, ManyToOne, ManyToMany

// FK 연결 끊기
    // User Entity
    @OneToMany(mappedBy = "user",fetch = FetchType.LAZY) // mappedby는 OneToMany쪽에서 연관관계의 주인을 설정하는 기능. 여기서 user는 상대 Entity의 필드이름이다.
    private List<QrCoupon> qrCoupons = new ArrayList<>();

    // QrCoupon Entity
    @ManyToOne(fetch =FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false, foreignKey = @ForeignKey(ConstraintMode.NO_CONSTRAINT))  // 물리적FK 제거 
    private User user;


// @ElementCollection
    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(name = "partner_roles",joinColumns = @JoinColumn(name= "partner_id", referencedColumnName = "id"))
    private List<String> roles;


    
// @Fetch : FetchMode.EAGER, LAZY
// @Valid : 유효성 검사
