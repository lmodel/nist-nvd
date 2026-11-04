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
  A statement of which product configurations have the vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdConfiguration  {

  private String operator;
  private Boolean negate;
  private List<NvdConfigurationNode> nodes;


}