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
  One SSVC decision, as the answers chosen on the way through a decision tree.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdSsvcData  {

  private ZonedDateTime timestamp;
  private String computed;
  private List<NvdSsvcOption> options;
  private String role;
  private String version;
  private Object decisionTree;
  private String id;
  private URI decisionTreeUrl;
  private String generator;


}