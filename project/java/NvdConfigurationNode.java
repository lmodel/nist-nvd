package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One part of a configuration statement, as a set of CPE matches.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdConfigurationNode  {

  private String operator;
  private Boolean negate;
  private List<NvdCpeMatch> cpeMatch;


}