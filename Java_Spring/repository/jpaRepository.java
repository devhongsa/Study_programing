// JDBC repository는 class로 만들고 JPA는 interface로 만든다
@Repository
public interface Repository extends JpaRepository<Account, Long> {
    Optional<Account> findFirstByOrderByIdDesc();

    Integer countByAccountUser(AccountUser accountUser);

    Optional<Account> findByAccountNumber(String accountNumber);

    List<Account> findByAccountUser(AccountUser accountUser);

    // fetch join
    @Query("select p from Partner p join fetch p.roles WHERE p.name = :name")
    Optional<Partner> findByName(@Param("name") String name);

    @Query("select f from CouponFeed f left join fetch f.participants where f.id = :feed_id")
    Optional<CouponFeed> findById(@Param("feed_id") Long feed_id);

    @Query("select f from CouponFeed f left join fetch f.participants where f.category = :category")
    List<CouponFeed> findByCategory(@Param("category") String category);

    // join
    @Query("SELECT p.templates FROM Partner p WHERE p.id = :partnerId")
    List<CouponTemplate> findTemplatesByPartnerId(@Param("partnerId") Long partnerId);

    @Query("SELECT p.userId FROM CouponFeed f LEFT JOIN FeedParticipants p ON f.id = p.feedId WHERE f.amount > :amount")
    Optional<List<Long>> findParticipantsByAmountGreaterThan(@Param("amount") Long amount);

}