@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
// @EntityListeners(value = {AuditingEntityListener.class})
public class BaseEntity {
    @CreatedDate
    private LocalDateTime createdAt;
    @LastModifiedDate
    private LocalDateTime updatedAt;
}

// config 에서 JpaAuditingConfiguration 설정해줘야한다.
// @EnableJpaAuditing을 설정해줌으로써 자동으로 생성일과 수정일을 관리해준다.

// @Column : name, length, nullable, unique
// @Id
// @GeneratedValue : strategy = GenerationType.IDENTITY
// @Transient : 데이터베이스에 저장하지 않을 컬럼.
// @Enumerated : EnumType.STRING, ORDINALㄴ
// @Table
// @JoinColumn : FK 지정 관련
// @OneToOne, OneToMany, ManyToOne, ManyToMany
// @ElementCollection
// @Fetch : FetchMode.EAGER, LAZY
// @Valid : 유효성 검사
