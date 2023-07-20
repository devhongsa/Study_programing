// JDBC repository는 class로 만들고 JPA는 interface로 만든다
@Repository
public interface Repository extends JpaRepository<Account, Long> {
    Optional<Account> findFirstByOrderByIdDesc();

    Integer countByAccountUser(AccountUser accountUser);

    Optional<Account> findByAccountNumber(String accountNumber);

    List<Account> findByAccountUser(AccountUser accountUser);

    @Query("select p from Partner p join fetch p.roles WHERE p.name = :name")
    Optional<Partner> findByName(@Param("name") String name);

    @Query("SELECT p.templates FROM Partner p WHERE p.id = :partnerId")
    List<CouponTemplate> findTemplatesByPartnerId(@Param("partnerId") Long partnerId);

}